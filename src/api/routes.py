from __future__ import annotations

from flask import Blueprint, jsonify, request, current_app

from src.utils.pdf_loader import load_pdf_text
from src.workflows.extraction_flow import ExtractionWorkflow


def create_api_blueprint(workflow: ExtractionWorkflow) -> Blueprint:
    api = Blueprint("api", __name__)

    @api.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @api.route("/extract", methods=["POST"])
    def extract():
        payload = request.get_json(silent=True) or {}
        text = (payload.get("text") or "").strip()
        pdf_path = (payload.get("pdf_path") or "").strip()
        metadata = payload.get("metadata") or {}

        if not text and pdf_path:
            try:
                text = load_pdf_text(pdf_path)
            except Exception as exc:
                current_app.logger.exception("PDF extraction failed")
                return jsonify({"error": "pdf_extraction_failed", "detail": str(exc)}), 400

        if not text:
            return jsonify({"error": "text is required"}), 400

        try:
            result = workflow.run_from_text(text, metadata=metadata)
        except Exception as exc:
            current_app.logger.exception("LLM extraction failed")
            return jsonify({"error": "extraction_failed", "detail": str(exc)}), 500

        return jsonify(result), 200

    return api
