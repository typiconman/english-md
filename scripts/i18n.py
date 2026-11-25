"""Interface strings.

The site's chrome is in English, like the texts.  The keys are the same as in the
Church Slavonic library (slavonic/cu-md-sandbox), which is bilingual; to add a
language there, see its i18n.py.
"""

LANGS = ("en",)

STRINGS = {
    "skip": "Skip to the text",
    # library page
    "tagline": "Orthodox service books in English. Read them on any screen, copy the text into your own documents, or print it.",
    "find_book": "Find a book",
    "find_placeholder": "Title or month",
    "all_books": "All books",
    "no_match": "No book matches. Try a shorter word, or clear the search.",
    "clear_search": "Clear search",
    "books_count": "{n} books",
    "read": "Read",
    "scan": "Page scans",
    "scan_short": "Scan",
    "contents": "Contents",
    "chapters_n": "{n} sections",
    "about_title": "About this library",
    "about_text": "The texts are kept as open data in Markdown on GitHub, the same way as the Church Slavonic texts of the Ponomar Library. Corrections are welcome.",
    "church_slavonic": "Church Slavonic texts",
    "source_on_github": "Texts on GitHub",
    "report_error": "Report an error",
    "supported_by": "Supported by the Slavonic Computing Initiative",
    # book page
    "edition": "Edition",
    "source_note": "Note",
    "start_reading": "Start reading",
    "pages_short": "pp.",
    "volume": "Volume",
    "library": "Library",
    # reader
    "open_contents": "Contents and library",
    "close": "Close",
    "this_book": "This book",
    "in_this_section": "In this section",
    "previous": "Previous",
    "next": "Next",
    "reading_settings": "Reading settings",
    "text_size": "Text size",
    "smaller": "Smaller text",
    "larger": "Larger text",
    "typeface": "Typeface",
    "theme": "Page color",
    "theme_light": "White",
    "theme_sepia": "Sepia",
    "theme_dark": "Dark",
    "page_numbers": "Page numbers",
    "pages_margin": "In the margin",
    "pages_inline": "In the text",
    "pages_hidden": "Hidden",
    "copy": "Copy",
    "copy_section": "Copy this section",
    "copied": "Copied. Paste it into Word or another editor.",
    "copy_failed": "Your browser blocked copying. Select the text and press Ctrl+C.",
    "print": "Print",
    "page_n": "Page {l} in the scan",
    "page_plain": "Page {l}",
    "note": "Note",
    # scan viewer
    "scan_of": "Scan",
    "back_to_text": "Back to the text",
    "show_in_text": "Show this page in the text",
    "open_full": "Open full screen",
    "download_pdf": "Download PDF",
    "viewer_failed": "The page viewer did not start. You can open the PDF directly instead.",
    "open_pdf": "Open the PDF",
    "scan_missing": "This book has no page scans yet.",
    "close_scan": "Close the scan",
}


def table():
    """{"en": {key: str}} for the JavaScript side."""
    return {"en": dict(STRINGS)}
