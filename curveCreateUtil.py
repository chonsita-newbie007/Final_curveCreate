import json
from maya import cmds
from maya import mel

def process_user_selection(data):
    select_mode = data.get("Selection")
    name_mode = data.get("Name", {}).get("Mode")
    custom_name = data.get("Name", {}).get("CustomName")
    shape = data.get("Shape")
    options = data.get("Options", {})

    #forOptionPart_changeToBoolean
    snap_to_joint = bool(options.get("SnapToJoint"))
    create_group = bool(options.get("CreateGroup"))
    create_main_control = bool(options.get("CreateMainControl"))

    #warningPart
    if select_mode is None:
        cmds.warning("⚠️ Please select either 'Hierarchy' or 'Selection'")
        return
    if name_mode == "Custom" and not custom_name:
        cmds.warning("⚠️ Please enter a custom name")
        return

    #outPutData
    print("\n===== Curve Creator Selection =====")
    print(f"Joint Selection : {select_mode}")
    print(f"Name Mode       : {name_mode}")
    if custom_name:
        print(f"Custom Name     : {custom_name}")
    print(f"Shape           : {shape}")
    print("Options:")
    for key, val in options.items():
        print(f"   {key}: {val}")
    print("===================================\n")

    #getFirstName
    def normalize_creator_result(result):
        if isinstance(result,(list,tuple)) and result:
            return result[0]
        return result

#---------------------------------------------------------------------------------#
    #curvePart
    def circleCreate_curve():
        return cmds.circle(name='circle_ctrl', nr=(0, 1, 0), r=1)[0]

    def cubeCreate_curve():
        cube = ('curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 ;')
        cube_curve = mel.eval(cube)
        return cube_curve

    def eyeCreate_curve():
        ctr_crvpoints_pos = {'center.cv[0]': [-1.3225501652685798, 1.0034237306524114, -0.1362164032839753], 
                            'center.cv[1]': [-1.1452703252895788e-16, 1.0598754234905174e-05, -0.13621640328397522], 
                            'center.cv[2]': [1.3225501652685798, 1.003423730652411, -0.13621640328397513], 
                            'center.cv[3]': [1.870368380641604, 9.696022713476625e-17, -0.1362164032839751], 
                            'center.cv[4]': [1.3225501652685798, -1.0034237306524112, -0.13621640328397513], 
                            'center.cv[5]': [1.8735607989237765e-16, -1.059875423602945e-05, -0.13621640328397522], 
                            'center.cv[6]': [-1.3225501652685798, -1.003423730652411, -0.1362164032839753], 
                            'center.cv[7]': [-1.870368380641604, -2.5506147568249137e-16, -0.13621640328397533]}
        
        lft_crvpoints_pos = {'left.cv[0]': [-1.39401808061731, 0.3940180806173099, 0.1362164032839752], 
                            'left.cv[1]': [-1.0, 0.5572257134292149, 0.13621640328397522], 
                            'left.cv[2]': [-0.6059819193826901, 0.3940180806173098, 0.13621640328397525], 
                            'left.cv[3]': [-0.44277428657078477, 2.8886679382857757e-17, 0.13621640328397525], 
                            'left.cv[4]': [-0.6059819193826901, -0.39401808061730986, 0.13621640328397525], 
                            'left.cv[5]': [-0.9999999999999999, -0.5572257134292153, 0.13621640328397522], 
                            'left.cv[6]': [-1.39401808061731, -0.3940180806173098, 0.1362164032839752], 
                            'left.cv[7]': [-1.5572257134292151, -7.598867379629784e-17, 0.1362164032839752]}
        
        rgt_crvpoints_pos = {'right.cv[0]': [0.6059819193826901, 0.3940180806173099, 0.13621640328397522], 
                            'right.cv[1]': [1.0, 0.5572257134292149, 0.13621640328397522], 
                            'right.cv[2]': [1.39401808061731, 0.3940180806173098, 0.13621640328397522], 
                            'right.cv[3]': [1.5572257134292151, 2.8886679382857757e-17, 0.13621640328397522], 
                            'right.cv[4]': [1.39401808061731, -0.39401808061730986, 0.13621640328397522], 
                            'right.cv[5]': [1.0, -0.5572257134292153, 0.13621640328397522], 
                            'right.cv[6]': [0.6059819193826901, -0.3940180806173098, 0.13621640328397522], 
                            'right.cv[7]': [0.4427742865707849, -7.598867379629784e-17, 0.13621640328397522]}

        eye = mel.eval('circle -n "eye" -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]
        l_eye = mel.eval('circle -n "l_eye" -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]
        r_eye = mel.eval('circle -n "r_eye" -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]

        center_spans = cmds.getAttr(f'eye.spans')

        for i in range(center_spans):
            cvid = f'eye.cv[{i}]'
            pos = ctr_crvpoints_pos[cvid.replace('eye', 'center')]
            cmds.xform(cvid, t=pos, ws=True)

        for i in range(center_spans):
            cvid = f'l_eye.cv[{i}]'
            pos = lft_crvpoints_pos[cvid.replace('l_eye', 'left')]
            cmds.xform(cvid, t=pos, ws=True)

        for i in range(center_spans):
            cvid = f'r_eye.cv[{i}]'
            pos = rgt_crvpoints_pos[cvid.replace('r_eye', 'right')]
            cmds.xform(cvid, t=pos, ws=True)

        cmds.parent('l_eye', 'eye')
        cmds.parent('r_eye', 'eye')

        print("Created:", eye)
        return eye
#---------------------------------------------------------------------------------#
    
    #heirachyAndSelectPart
    def collect_joint_list(mode):
        result = []

        def walk(node):
            if cmds.nodeType(node) != "joint":
                return
            result.append(node)
            for c in cmds.listRelatives(node, children=True, fullPath=False) or []:
                walk(c)

        if mode == "Selection":
            for sel in cmds.ls(selection=True, long=False):
                if cmds.nodeType(sel) == "joint":
                    result.append(sel)
        elif mode == "Hierarchy":
            for sel in cmds.ls(selection=True, long=False):
                walk(sel)
        return result

#----------------------------------------------------------------------------------------------------------------------------
    #Name

    def sanitize_name(name):
        return name.replace('|', '_')

    def name(base, idx = None, use_match_joint=False):
        if use_match_joint:
            return base
        else:
            if idx is None:
                return base
            return f"{base}_{idx:04d}"

#----------------------------------------------------------------------------------------------------------------------------
    #snapPart
    def snap_transform_to_target(transform, target):
        try:
            mat = cmds.xform(target, q=True, ws=True, matrix=True)
            cmds.xform(transform, ws=True, matrix=mat)
        except Exception as e:
            try:
                t = cmds.xform(target, q=True, ws=True, translation=True)
                rot = cmds.xform(target, q=True, ws=True, rotation=True)
                cmds.xform(transform, ws=True, translation=t)
                cmds.xform(transform, ws=True, rotation=rot)
            except:
                cmds.warning(f"Cannot snap {transform} to {target}: {e}")

#----------------------------------------------------------------------------------------------------------------------------
    joints = collect_joint_list(select_mode)
    print("Collected joints:", joints) 

    if not joints and not create_main_control:
        cmds.warning("No Joint found for selected mode.")
        return

    create_control = []
    index = 1

    for joint in joints:

        ctrl_name = sanitize_name(joint)

        #nameSelected
        if name_mode == "Match Joint Name":
            ctrl_name = name(joint, use_match_joint=True)
        else:
            ctrl_name = name(custom_name, idx = index, use_match_joint = False)

        #shapeSelected
        if shape == 'Circle':
            new_ctrl = circleCreate_curve()
        elif shape == 'Cube':
            new_ctrl = cubeCreate_curve()
        elif shape == 'Eye':
            new_ctrl = eyeCreate_curve()
        else:
            cmds.warning(f"❌ Please select shape type")
            return

        ctrl = normalize_creator_result(new_ctrl)

        #rename
        final_name = ctrl_name
        if cmds.objExists(final_name):
            suffix = 1
            while cmds.objExists(f"{final_name}_{suffix:02d}"):
                suffix += 1
            final_name = f"{final_name}_{suffix:02d}"

        try:
            ctrl = cmds.rename(ctrl, final_name)
        except Exception:
            final_name = ctrl

        #option
        if create_group:
            grp_name = f"{final_name}_grp"
            if cmds.objExists(grp_name):
                gidx = 1
                while cmds.objExists(f"{grp_name}_{gidx:02d}"):
                    gidx += 1
                grp_name = f"{grp_name}_{gidx:02d}"

            grp = cmds.group(empty = True, name = grp_name)

            t = cmds.xform(joint, q=True, ws=True, translation=True)
            r = cmds.xform(joint, q=True, ws=True, rotation=True)
            cmds.xform(grp, ws=True, translation=t, rotation=r)

            if snap_to_joint:
                cmds.xform(ctrl, ws=True, translation=t, rotation=r)

            else:
                ctrl_pos = cmds.xform(ctrl, q=True, ws=True, rp=True)
                cmds.xform(grp, ws=True, piv=ctrl_pos)

            try:
                cmds.parent(ctrl,grp)
            except Exception:
                cmds.warning(f"Failed to parent {ctrl} under {grp}")

            cmds.xform(ctrl, t=(0,0,0), ro=(0,0,0))

        else:
            if snap_to_joint:
                snap_transform_to_target(ctrl, joint)
            else:
                ctrl_pos = cmds.xform(ctrl, q=True, ws=True, rp=True)
                cmds.xform(ctrl, ws=True, piv=ctrl_pos)
    
        create_control.append(final_name)
        index += 1

#------------------------------------------------------------------------------------------------------------------------------------------
    main_control = None
    if create_main_control:
        mc_name = "main_control_cc"
        if cmds.objExists(mc_name):
            midx = 1
            while cmds.objExists(f"{mc_name}_{midx:02d}"):
                midx += 1
            mc_name = f"{mc_name}_{midx:02d}"
        mc = circleCreate_curve()
        mc = normalize_creator_result(mc)
        try:
            mc = cmds.rename(mc, mc_name)
        except Exception:
            mc_name = mc_name
        main_control = mc_name
        create_control.append(main_control)

    print("Created controls:", create_control)
    return create_control