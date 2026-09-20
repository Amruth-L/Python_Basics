class Node:
    def __init__(self, page):
        self.page = page
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        self.current = Node(homepage)

    def visit(self, page):
        new_page = Node(page)

        self.current.next = new_page
        new_page.prev = self.current

        self.current = new_page

    def back(self):
        if self.current.prev:
            self.current = self.current.prev

    def forward(self):
        if self.current.next:
            self.current = self.current.next

    def show_current(self):
        print("Current page:", self.current.page)


# Create browser history
browser = BrowserHistory("Google")

browser.visit("YouTube")
browser.visit("GitHub")
browser.visit("ChatGPT")

browser.show_current()

browser.back()
browser.show_current()

browser.back()
browser.show_current()

browser.forward()
browser.show_current()