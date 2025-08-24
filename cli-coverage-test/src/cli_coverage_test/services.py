"""
Service modules demonstrating logger usage across the project.
"""

from .logger import get_logger

# Create a module-specific logger
logger = get_logger(__name__)


class ExampleService:
    """Example service class showing logger usage."""
    
    def __init__(self):
        self.logger = get_logger(f"{__name__}.{self.__class__.__name__}")
        self.logger.info("ExampleService initialized")
    
    def process_data(self, data):
        """Example method that processes data with logging."""
        self.logger.debug(f"Processing data: {data}")
        
        if not data:
            self.logger.warning("Empty data received")
            return None
        
        try:
            # Simulate some processing - convert to string to handle any data type
            result = len(str(data))
            self.logger.info(f"Successfully processed data, result: {result}")
            return result
            
        except Exception as e:
            self.logger.error(f"Failed to process data: {e}")
            raise


def example_function():
    """Example function demonstrating logger usage."""
    logger.info("Starting example function")
    
    service = ExampleService()
    
    # Test with valid data
    result = service.process_data("test data")
    logger.info(f"Function result: {result}")
    
    # Test with empty data
    result = service.process_data("")
    logger.info(f"Function result with empty data: {result}")
    
    logger.info("Example function completed")


if __name__ == "__main__":
    example_function()
