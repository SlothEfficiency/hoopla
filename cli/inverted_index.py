import os

from pickle import dump, load

from string_operations import handle_string

class InvertedIndex:
    def __init__(self):
        self.index = {}
        self.docmap = {}

    def __add_document(self, doc_id: int, text: str) -> None:
        tokens = handle_string(text)
        for token in tokens:
            if token in self.index.keys():
                self.index[token].append(doc_id)
            else:
                self.index[token] = [doc_id]

    def get_documents(self, term: str) -> list:
        term = term.lower()
        if term in self.index.keys():
            return sorted(self.index[term])
        else:
            return []
        
    def get_title_by_id(self, id: int) -> str:
        return self.docmap[id]
        
    def build(self, movies: list) -> None:
        for i, movie in enumerate(movies, start=1):
            self.__add_document(i, f"{movie['title']} {movie['description']}")
            self.docmap[i] = movie['title']

    def save(self) -> None:
        if not os.path.exists("cache/"):
            os.mkdir("cache/")

        with open("cache/index.pkl", "wb") as f:
            dump(self.index, f)

        with open("cache/docmap.pkl", "wb") as f:
            dump(self.docmap, f)


    def load(self) -> None:
        try:
            with open("cache/index.pkl", "rb") as f:
                self.index = load(f)
            with open("cache/docmap.pkl", "rb") as f:
                self.docmap = load(f)

        except Exception as e:
            raise(f"Error occured while loading: {e}")
        


        