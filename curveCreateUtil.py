import json
from maya import cmds
from maya import mel

def process_user_selection(data):
    select_mode = data.get("Selection")
    name_mode = data.get("Name", {}).get("Mode")
    custom_name = data.get("Name", {}).get("CustomName")
    shape = data.get("Shape")
    options = data.get("Options", {})

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

    json_data = json.dumps(data, indent=4)
    print("JSON Output:\n", json_data)

    # ---------------- nested functions ----------------
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
    # ---------------- end nested functions ----------------

    curve_name = None

    if shape == 'Circle':
        curve_name = circleCreate_curve()
    elif shape == 'Cube':
        curve_name = cubeCreate_curve()
    elif shape == 'Eye':
        curve_name = eyeCreate_curve()
    else:
        cmds.warning(f"❌ Please select shape type")
        return

    if curve_name:
        print(f"✅ Created curve: {curve_name}")
        if name_mode == "Custom" and custom_name:
            curve_name = cmds.rename(curve_name, custom_name)
            print(f"🔤 Rename to {curve_name}")

    return curve_name
