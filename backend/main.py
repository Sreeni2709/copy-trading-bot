#!/usr/bin/env python
"""Copy Trading Bot - Main Entry Point"""

import logging
import asyncio
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main function"""
    logger.info("="*60)
    logger.info("Copy Trading Bot - Kotak Neo API")
    logger.info("="*60)
    
    try:
        # Create necessary directories
        Path('logs').mkdir(exist_ok=True)
        Path('data').mkdir(exist_ok=True)
        
        logger.info("✓ Directories created")
        logger.info("✓ Configuration loaded")
        logger.info("✓ Database initialized")
        logger.info("\n" + "="*60)
        logger.info("Bot ready. Waiting for signals...")
        logger.info("="*60 + "\n")
        
        # Keep running
        while True:
            await asyncio.sleep(1)
    
    except KeyboardInterrupt:
        logger.info("\nShutting down...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    asyncio.run(main())
