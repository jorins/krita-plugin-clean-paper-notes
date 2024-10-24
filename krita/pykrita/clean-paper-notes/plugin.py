from time import sleep
from krita import *
from .filters import pencil, ink


class CleanPaperNotes(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            "cleanPaperNotes",
            "Clean paper notes",
            "tools/scripts"
        )

        menu = QtWidgets.QMenu("cleanPaperNotes", window.qwindow())
        action.setMenu(menu)

        actionPencilSingle = window.createAction(
            "cleanPaperNotesPencilSingle",
            "Pencil, single document",
            "tools/scripts/cleanPaperNotes"
        )

        # actionPencilBatch = window.createAction(
        #     "cleanPaperNotesPencilBatch",
        #     "Pencil, all open documents",
        #     "tools/scripts/cleanPaperNotes"
        # )

        actionInkSingle = window.createAction(
            "cleanPaperNotesInkSingle",
            "Ink, single document",
            "tools/scripts/cleanPaperNotes"
        )

        # actionInkBatch = window.createAction(
        #     "cleanPaperNotesInkBatch",
        #     "Ink, all open documents",
        #     "tools/scripts/cleanPaperNotes"
        # )

        actionPencilSingle.triggered.connect(self.pencilSingle)
        # actionPencilBatch.triggered.connect(self.pencilBatch)
        actionInkSingle.triggered.connect(self.inkSingle)
        # actionInkBatch.triggered.connect(self.inkBatch)

    def pencilSingle(self):
        self.single(pencil())

    def pencilBatch(self):
        self.batch(pencil())

    def inkSingle(self):
        self.single(ink())

    def inkBatch(self):
        self.batch(ink())

    def single(self, filters):
        app = Krita.instance()
        doc = app.activeDocument()
        bounds = doc.bounds().getRect()
        layer = doc.activeNode()
        for filter in filters:
            filter.apply(layer, *bounds)

        # app.action('selectopaque').trigger()
        # doc.refreshProjection()
        # sleep(0.2)  # Race condition workaround (:
        # app.action('resizeimagetoselection').trigger()
        doc.refreshProjection()

    def batch(self, filters):
        return

        # app = Krita.instance()
        # docs = app.documents()
        #
        # for doc in app.documents:
        #     # switch to target
        #     # set batch proc
        #     self.single(filters)
        #     # save


Krita.instance().addExtension(CleanPaperNotes(Krita.instance()))
