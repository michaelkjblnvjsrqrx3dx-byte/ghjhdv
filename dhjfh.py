for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == target_filename:
                full_path = os.path.normpath(os.path.join(root, file))
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    if search_text in content:
                        content = content.replace(search_text, replace_text)
                        with open(full_path, "w", encoding="utf-8") as f:

                    with open(full_path, "r",
