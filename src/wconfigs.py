"""
Here tkinter widget 
configurations and grid 
positioning parameters

"""
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
            "activeforeground": "#fff"
        },
        "grid": {
            "row": 2,
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
            "activebackground": "#bebebe"
        },
        "grid": {
            "row": 1,
            "column": 3,
            "padx": (10, 50),
            "pady": (10, 10),
            "sticky": "nswe",
            "ipadx": 10,
            "ipady": 5
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
            "columnspan": 2,
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
            "columnspan": 2,
            "padx": 10,
            "pady": (10, 10),
            "ipady": 5,
        }
    },
}
