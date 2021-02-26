# Кнофиг внешнего вида элементов интерфейса

configs = {
    "LabelFolderPath": {
        "config": {
            "text": "Folder"
        },
        "grid": {
            "row": 0,
            "column": 0,
            "padx": (50, 10),
            "pady": (80, 10),
            "sticky": 'w'
        }
    },
    "LabelExportPath": {
        "config": {
            "text": "Export"
        },
        "grid": {
            "row": 1,
            "column": 0,
            "padx": (50, 10),
            "pady": (10, 10),
            "sticky": 'w'
        }
    },
    "ButtonRun": {
        "config": {
            "text": "Start hashing",
            "bg": "#0071bd",
            "bd": 0,
            "activebackground": "#0083da",
            "height": 2,
            "fg": "#ffffff",
            "cursor": "hand2",
        },
        "grid": {
            "row": 4,
            "column": 0,
            "columnspan": 4,
            "sticky": "nswe",
            "padx": (50, 50),
            "pady": (10, 80)
        }
    },
    "ButtonRunInProcess": {
        "config": {
            "text": "In process",
            "bg": "#d1d1d1",
            "bd": 0,
            "activebackground": "#bebebe",
            "height": 2,
            "fg": "#ffffff",
            "cursor": "hand2",
        },
        "grid": {
            "row": 4,
            "column": 0,
            "columnspan": 4,
            "sticky": "nswe",
            "padx": (50, 50),
            "pady": (10, 80)
        }
    },
    "ButtonSelectFolder": {
        "config": {
            "text": "Select folder",
            "bg": "#d1d1d1",
            "bd": 0,
            "activebackground": "#bebebe",
            "cursor": "hand2"
        },
        "grid": {
            "row": 0,
            "column": 3,
            "padx": (10, 50),
            "pady": (80, 10),
            "sticky": "nswe",
            "ipadx": 10,
            "ipady": 5
        }
    },
    "ButtonSelectExport": {
        "config": {
            "text": "Select export",
            "bg": "#d1d1d1",
            "bd": 0,
            "activebackground": "#bebebe",
            "cursor": "hand2",
            "width": 10
        },
        "grid": {
            "row": 1,
            "column": 3,
            "padx": (10, 50),
            "pady": (10, 10),
            "sticky": "nswe",
            "ipadx": 10,
            "ipady": 5,
        }

    },
    "EntrySelectFolder": {
        "config": {
            "width": 50,
            "bd": 1
        },
        "grid": {
            "row": 0,
            "column": 1,
            "padx": 10,
            "pady": (80, 10),
            "ipady": 5,
        }
    }, "EntrySelectExport": {
        "config": {
            "width": 50,
            "bd": 1
        },
        "grid": {
            "row": 1,
            "column": 1,
            "padx": 10,
            "pady": (10, 10),
            "ipady": 5,
        }
    }, "CheckButtonSeparated": {
        "config": {
            "text": "File for each subdir",
            "bd": 0,
            "cursor": "hand2"
        },
        "grid": {
            "row": 2,
            "column": 0,
            "columnspan": 4,
            "padx": (50, 0),
            "pady": (0, 10),
            "sticky": "w",
        }
    }, "CheckButtonVerify": {
        "config": {
            "text": "Verify mode",
            "bd": 0,
            "cursor": "hand2"
        },
        "grid": {
            "row": 3,
            "column": 0,
            "columnspan": 4,
            "padx": (50, 0),
            "pady": (0, 10),
            "sticky": "w",
            "columnspan": 1,
        }
    }
}
