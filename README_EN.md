# YouTube Massive Downloader

[English](README_EN.md) | [Español](README.md)

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-red.svg)
![Status](https://img.shields.io/badge/status-Stable-green.svg)

YouTube Massive Downloader is a reverse engineering tool designed for mass downloading entire YouTube channels. It utilizes an Anonymous Hybrid Layer architecture that bypasses modern Google restrictions without the need for cookies or manual authentication.

## Why this version is unique

Most downloaders (including basic yt-dlp) currently fail with errors such as 403 Forbidden or Sign in to confirm you're not a bot. This software solves these issues by splitting the process into two isolated phases:

1. Metadata Extraction (Scrapetube): Retrieves IDs and Titles through pure JSON requests from the YouTube API, without loading tracking scripts or web interfaces.
2. Shielded Delivery (yt-dlp + Android App Profile): Performs streaming by simulating an official Android application (Pixel 8 Pro), bypassing the page rendering that triggers security blocks.

## Main Features

* Auto-Folder System: Automatically creates folders named after the channel and organizes the videos inside.
* High Definition (1080p/4K): Prioritizes the highest available quality (requires FFmpeg).
* Stealth Mode: Does not require browser cookies, avoiding the risk of personal account banning.
* Signature Bypass (PO Token): Uses mobile device profiles to skip browser token validation.

## Critical Requirements

Correct operation of the software requires:

1. Python 3.9 or higher
2. FFmpeg (Mandatory for quality higher than 720p):
   * Windows: winget install ffmpeg
   * Linux: sudo apt install ffmpeg

## Quick Start Guide

1. Install dependencies:
   ```bash
   pip install yt-dlp scrapetube
   ```
2. Run the script:
   ```bash
   python downloader.py
   ```
3. Enter URL: Paste the channel link (e.g., https://www.youtube.com/@ExampleChannel) and the process will begin automatically.

## Troubleshooting

| Problem | Cause | Solution |
| :--- | :--- | :--- |
| Low Quality (360p/720p) | Missing FFmpeg | Run winget install ffmpeg and restart your terminal. |
| Metadata Error | Temporary IP Block | Restart your router to obtain a new IP address. |
| Channel Not Found | Incorrect URL | Ensure you are using the @username format. |

## Disclaimer

This project is intended for educational purposes and personal backup only. The author is not responsible for any misuse of this tool. Always respect copyright and the platform's terms of service.

---
**Developed by @IvanTrujilloTech**
