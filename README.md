# FileBot---Auto-Python-Script

## Overview

This script monitors a directory, unzips files larger than a specified size (**X GB**), processes them, and deletes the zip files when finished. Originally developed for use with [Torrent Safe](https://torrentsafe.com) downloads, this script automates file management tasks with minimal user intervention.

While the script isn't polished or fully developed, it is functional and achieves the following tasks:
- Monitors a directory for downloaded files.
- Automatically unzips and processes files.
- Renames, moves, and cleans up files after processing.

## Usage Example

I personally use this script to monitor a download folder on a server. Using my phone, I download video files via Torrent Safe. Once the files are downloaded via HTTPS to the server, this script automatically handles the unzipping, processing, and cleanup. 

## Notes

- This script is **designed to be simple and specific** to certain needs. It may require modifications for your use case.
- Contributions via pull requests (PRs) are encouraged to enhance functionality or improve implementation.
- The script is a quick solution for a personal need, so it's not fully optimized or robust for all scenarios.

## Suggestions for Customization

You can adapt this script to suit your own requirements, such as:
- Setting thresholds for file size to trigger unzipping.
- Adjusting the directory monitoring behavior.
- Integrating additional processing or organizational steps.

I hope this script helps someone with a similar need. Feel free to share your improvements!

![alt text](https://raw.githubusercontent.com/pir8radio/FileBot---Auto-Python-Script/main/Screenshot%202024-07-28%20181256.jpg)
