from aqt.models import Models
from aqt.utils import getText
from aqt.models import AddModel

def onRename(self):
    """Ask the user for a new name for the model. Save it."""
    #difference: don't recompute requirements
    txt = getText(_("New name:"), default=self.model['name'])
    if txt[1] and txt[0]:
        self.model['name'] = txt[0]
        self.mm.save(self.model, recomputeReq=False)# only difference is recomputeReq=False
    self.updateModelsList()
Models.onRename = onRename

def modelChanged(self):
    """Called if the selected model has changed, in order to change self.model"""
    # difference: don't save the model, when it is selected
    #two lines deleted
    idx = self.form.modelsList.currentRow()
    self.model = self.models[idx]
Models.modelChanged = modelChanged
