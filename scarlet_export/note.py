from json import loads

class Note:
    """
    A Scarlet Notes note model. Has six properties: `uuid`, `folder`,
    `updateTimestamp`, `timestamp`, `tags`, and `content`.

    The timestamps are both ints in Unix time. UUID and folder are both
    strings. `content` is a string containing all of the note content.
    """
    def __init__(self, note):
        self.uuid = note['uuid']
        self.folder = note['folder']
        self.updateTimestamp = int(note['updateTimestamp'])
        self.timestamp = int(note['timestamp'])
        self.tags = note['tags'].split(',')
        noteContent = loads(note['description'])
        self.content = noteContent['note'][0]['text']
