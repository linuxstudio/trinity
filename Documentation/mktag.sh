#!/bin/bash
git log --pretty=format:"%h %cn %cd" | head -n 1 > tag
