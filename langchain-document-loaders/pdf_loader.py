from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader("dl-curriculum.pdf")
docs = loader.load()

print(f"Total pages: {len(docs)}\n")

# Loop through each page
for i, doc in enumerate(docs):
    # Clean problematic characters for Windows console
    safe_text = doc.page_content.encode("ascii", errors="ignore").decode()

    print(f"--- Page {i + 1} ---")
    print(f"Metadata: {doc.metadata}")
    print(f"Preview: {safe_text[:300]}...\n")  # Show first 300 characters
