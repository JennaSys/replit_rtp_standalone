from appTheme import theme, useStyle, ListButton, StyledButton
from pyreact import useState, render, component, Form, Span
from pymui import Button, List, ListItem, Typography, Box, TextField
from pymui import Paper, Container, AppBar, ThemeProvider, useTheme


@component
def App():
    newItem, setNewItem = useState("")
    editItem, setEditItem = useState("")
    listItems, setListItems = useState([])

    def handleSubmit(event):
        event.preventDefault()
        new_list = list(listItems)  # Make a copy
        if len(editItem) > 0:  # In edit mode
            new_list[new_list.index(editItem)] = newItem
        else:  # In add mode
            new_list.append(newItem)  # Add the new item
        setListItems(new_list)  # Update our state
        setNewItem("")  # Clear the new item value
        setEditItem("")  # Clear the edit item value

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    def handleDelete(item):
        new_list = list(listItems)  # Make a copy
        new_list.remove(item)  # Remove the specified item
        setListItems(new_list)  # Update our state

    def handleEdit(item):
        setNewItem(item)  # Set the new item value
        setEditItem(item)  # Set the edit item value

    @component
    def ItemVu(props):
        item = props['item']
        theme = useTheme()
        specialColor = theme['palette']['special']['main']
        classes = useStyle({'bgcolor': specialColor})

        return ListItem({'dense': True},
                  Button(
                     {'color': 'secondary',
                      'className': classes.root,
                      'onClick': lambda: handleDelete(item)
                     },
                     Span({'className': 'material-icons'}, 'delete'),
                     "Delete"
                    ),
                  StyledButton(
                     {'color': 'primary',
                      'onClick': lambda: handleEdit(item)
                     },
                     Span({'className': 'material-icons'}, 'edit'),
                     "Edit"
                    ),
                  Typography({'style': {'color': specialColor}}, item)
                 )

    @component
    def ListItemsVu():
        return [ItemVu({'key': item, 'item': item}) for item in listItems]

    if len(editItem) == 0:
        editColor = 'secondary'
        editLabel = "Add Item:"
    else:
        editColor = 'primary'
        editLabel = "Edit Item:"

    return ThemeProvider({'theme': theme},
              Container({'maxWidth': 'sm'},
                 AppBar({'position': 'static',
                             'style': {'marginBottom': '0.5rem'}
                            },
                    Box({'width': '100%', 'marginLeft': '0.5rem'},
                       Typography({'variant': 'h6'}, "React to Python")
                      )
                   ),
                 Paper({'elevation': 2},
                    Form({'onSubmit': handleSubmit,
                                'style': {'marginLeft': '1rem'}
                               },
                       TextField({'InputLabelProps': {'color': editColor},
                                      'label': editLabel,
                                      'value': newItem,
                                      'onChange': handleChange,
                                      'autoFocus': True
                                     }
                         ),
                       Button({'type': 'submit',
                                   'size': 'medium'
                                  }, "Submit"),
                      ),
                    List(None,
                       ListItemsVu(None)
                      ),
                   )
                )
             )

render(App, None, 'root')
