from app.logger import setup_logger

logger = setup_logger()

def clean_data(numbers):
    logger.info(f"Cleaning data: {numbers}")
    cleaned = [x for x in numbers if x is not None and x >= 0]
    logger.info(f"Cleaned data: {cleaned}")
    return cleaned


def compute_statistics(numbers):
    logger.info(f"Computing statistics for: {numbers}")

    if len(numbers) == 0:
        logger.error("Empty list provided to compute_statistics")
        raise ValueError("Empty list")

    mean = sum(numbers) / len(numbers)

    stats = {
        "mean": mean,
        "min": min(numbers),
        "max": max(numbers)
    }

    logger.info(f"Computed stats: {stats}")
    return stats