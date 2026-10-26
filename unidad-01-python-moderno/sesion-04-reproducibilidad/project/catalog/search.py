import json
import logging
from pathlib import Path
from pydantic import ValidationError
from catalog.models import Course

logger = logging.getLogger(__name__)


def search_courses(query: str, catalog_path: Path | str | None = None) -> list[Course]:
    if not query.strip():
        raise ValueError("Query string cannot be empty or blank")

    if catalog_path is None:
        catalog_path = Path(__file__).resolve().parents[1] / "data" / "courses.json"
    else:
        catalog_path = Path(catalog_path)

    logger.debug("Reading catalog: %s", catalog_path)

    try:
        with open(catalog_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            courses = [Course(**item) for item in raw_data]
    except (FileNotFoundError, json.JSONDecodeError, ValidationError) as e:
        logger.error("Error loading catalog from %s: %s", catalog_path, e)
        raise

    clean_query = query.strip().casefold()
    matches = [c for c in courses if clean_query in c.title.casefold()]

    # Único cambio para el Ejercicio 4:
    logger.info(
        "Search completed: %d matches out of %d total courses",
        len(matches),
        len(courses),
    )

    return matches
