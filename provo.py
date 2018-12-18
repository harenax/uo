def newprovo():
    pass
    
def provo():
    # Clear previous targets and remove target finger
    prov1 = prov2 = 0
    Target.ClearLastandQueue()
    Target.Cancel()

    # Find first target
    Target.SetLastTargetFromList("nearestenemy")
    Target.TargetExecute(prov1)
    prov1 = Target.GetLast()

    # Find second target - chose furthest to get them away from me
    Target.SetLastTargetFromList("furthestenemy")
    Target.TargetExecute(prov2)
    prov2 = Target.GetLast()
    
    # And make them attack each other!
    Player.UseSkill("Provocation")
    Target.WaitForTarget(500, True)
    Target.TargetExecute(prov1)
    Target.WaitForTarget(500, True)
    Target.TargetExecute(prov2)

    # Clear previous targets and remove target finger
    Target.Cancel()
    Target.ClearLastandQueue()
    prov1 = prov2 = 0
    
provo()

