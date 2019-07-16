from json import loads

class Note:
    """
    A Scarlet Notes note model. Has six properties: `uuid`, `folder`,
    `updateTimestamp`, `timestamp`, `tags`, and `content`.

    The timestamps are both ints in Unix time. UUID and folder are both
    strings. `content` is a string containing all of the note content.

    `tags` and `folders` are both dictionaries where keys are UUIDs and
    values are the actual titles.
    """
    def __init__(self, note, tags, folders):
        self.uuid = note['uuid']
        # folders are only available since Scarlet v6
        if 'folder' in note:
            if note['folder'] != '':
                self.folder = folders[note['folder']]
        else: self.folder = ''
        self.updateTimestamp = int(note['updateTimestamp'])
        self.timestamp = int(note['timestamp'])
        self.tags = []
        for tag in note['tags'].split(','):
            if tag != '':
                self.tags.append(tags[tag])
        noteContent = loads(note['description'])['note']
        # note headings are optional in Scarlet
        if len(noteContent) > 1:
            self.title = noteContent[0]['text']
            self.content = noteContent[1]['text']
        else:
            self.content = noteContent[0]['text']
            self.title = ''
