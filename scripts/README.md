# ASC ros wrapper

This directory contains initial version of ASC ros wrapper. This code works as followed.

1) PerceptionWrapper, SceneDescriptorWrapper, ActionEffectWrapper, AffordanceWrapper are initialized.
2) Each of this wrapper have two rostopics:
  * NodeLister: List Each node connected to the wrapper.
  * NewNodeListener: For Connecting to the wrapper.
3) For each of this wrapper lists nodes connected to them to their specific rostopic.

    Sample NodeInfo:
    nodeId: DummyLeverUp
    purposeId: Lever_Up_Mask
    nodeTopic: lever_up_locations
    description: This is simple scene descriptor that shows where object leveruppable.

4) When a node needs a model that gives Lever_Up_Mask(purposeId), it can connect to this node by parsing the NodeInfo List.
