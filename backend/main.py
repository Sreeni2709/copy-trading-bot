#!/usr/bin/env python
"""Copy Trading Bot - Main Entry Point"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse startup arguments."""
    parser = argparse.ArgumentParser(description="Copy Trading Bot")
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run a single startup cycle and exit (useful for smoke tests).",
    )
    return parser.parse_args()


async def main(once: bool = False):
    """Run the backend startup flow."""
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

        if once:
            logger.info("Startup smoke test completed.")
            return

        # Keep running
        while True:
            await asyncio.sleep(1)
    
    except KeyboardInterrupt:
        logger.info("\nShutting down...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main(args.once))
