import sys
import io

# Set UTF-8 encoding for stdout to handle Unicode characters
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

# Handle Unicode characters properly for Windows console
try:
    print(result[1].page_content)
except UnicodeEncodeError:
    # Fallback: encode as UTF-8 and decode, or use repr for debugging
    print(repr(result[1].page_content))