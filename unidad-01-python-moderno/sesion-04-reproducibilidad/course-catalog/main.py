import sys
from catalog.logging_config import setup_logging
from catalog.search import search_courses

def main():
    # Inicializar logs en nivel INFO (o tomar el nivel de sys.argv)
    setup_logging(level="INFO")
    
    query = sys.argv[1] if len(sys.argv) > 1 else "python"
    results = search_courses(query)
    
    for course in results:
        print(f"- {course.code}: {course.title}")

if __name__ == "__main__":
    main()