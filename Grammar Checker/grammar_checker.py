import language_tool_python

# Create grammar checker
tool = language_tool_python.LanguageTool('en-US')

print("=" * 50)
print("       GRAMMAR CHECKER")
print("=" * 50)

# Get text from user
text = input("\nEnter a sentence or paragraph:\n")

# Check grammar
matches = tool.check(text)

print("\n" + "=" * 50)
print("GRAMMAR ANALYSIS")
print("=" * 50)

if len(matches) == 0:
    print("\n✅ No grammar mistakes found!")
else:
    print(f"\n❌ Found {len(matches)} possible mistake(s).\n")

    for i, match in enumerate(matches, 1):
        print(f" mistake {i}:")
        print("Message:", match.message)

        if match.replacements:
            print("Suggestion:", match.replacements[0])

        print("Position:", match.offset)
        print("-" * 40)

# Corrected sentence
corrected_text = tool.correct(text)

print("\nOriginal Text:")
print(text)

print("\nCorrected Text:")
print(corrected_text)

print("\n" + "=" * 50)
print("       CHECK COMPLETED")
print("=" * 50)