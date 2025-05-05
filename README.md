# PyFileHandle

### How it works:

1. **File Reading**: We open the file using `with open()` (this ensures that the file is properly closed after reading). We use `'r'` mode for reading.
2. **File Writing**: We open another file in `'w'` mode to write the modified contents. If the file doesn’t exist, it will be created automatically.
3. **Error Handling**: We catch:

   * `FileNotFoundError` if the file doesn't exist.
   * `IOError` if there’s an issue with reading or writing.
   * A general `Exception` to catch any other unexpected errors.

