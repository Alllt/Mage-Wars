class MockCard:
    def __init__(self, **props):
        self._id = props.get("_id", 1)
        self.Name = props.get("Name", "MockCard")
        self.name = self.Name
        self.Type = [t.strip() for t in props.get("Type", "").split(",") if t.strip()]
        self.controller = props.get("controller", "Player1")
        self.Position = (0, 0)
        self.isFaceUp = props.get("isFaceUp", True)
        self.orientation = props.get("orientation", "Rot0")
        self.isDestroyed = props.get("isDestroyed", False)
        self.markers = self.markers = props.get("markers", {})
        self.Bindings = []
        self.Attachments = []
        self.bTraits = props.get("bTraits", "").split(",") if "bTraits" in props else []
        self.zTraits = props.get("zTraits", "").split(",") if "zTraits" in props else []
        self.nativeTraits = props.get("nativeTraits", "") if "nativeTraits" in props else ''
        self.attachedTraits = props.get("attachedTraits", "") if "attachedTraits" in props else ''
        self.tokenTraits = props.get("tokenTraits", "") if "tokenTraits" in props else ''
        self.equipmentTraits = props.get("equipmentTraits", "") if "equipmentTraits" in props else ''
        self.zoneTraits = props.get("zoneTraits", "") if "zoneTraits" in props else ''
        self.arenaTraits = props.get("arenaTraits", "") if "arenaTraits" in props else ''
        self.tempTraits = props.get("tempTraits", "") if "tempTraits" in props else ''
        self.EOATraits = props.get("EOATraits", "") if "EOATraits" in props else ''
        
        self.properties = props  # catch-all for anything else

    def moveToTable(self, x, y, faceUp=True, index=0, isScriptMove=True):
        self.Position = (x, y)
        self.isFaceUp = faceUp

    def getProperty(self, name):
        return self.properties.get(name, None)

    def setProperty(self, name, value):
        self.properties[name] = value
        if name == "Type":
            self.Type = [t.strip() for t in value.split(",")]
        elif name == "bTraits":
            self.bTraits = value.split(",")
        elif name == "zTraits":
            self.zTraits = value.split(",")

    def __getattr__(self, name):
        # Fallback to dynamic property dict
        return self.properties.get(name, None)

    def __contains__(self, item):
        # For compatibility like 'Attack' in card.Type
        return item in self.Type

    def __str__(self):
        return self.Name
