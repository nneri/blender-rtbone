import bpy
import numpy as np
import mathutils

def setVertexGroup(selected):
    for i in range(len(selected)):
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action='DESELECT')
        s = selected[i]
        bpy.context.view_layer.objects.active = s
        name = "frag" + str(i)
        if name not in s.vertex_groups.keys():
            vg = s.vertex_groups.new(name=name)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.object.vertex_group_assign()
    bpy.ops.object.mode_set(mode="OBJECT")

def createArmature(selected):
    bpy.ops.object.add(type='ARMATURE', enter_editmode=True, location=(0,0,0))
    amt = bpy.context.object
    amt.name = "PhysicsObjectAmt"
    bpy.ops.armature.select_all(action='SELECT')
    bpy.ops.armature.delete()
    bpy.ops.object.mode_set(mode='EDIT')
    for i in range(len(selected)):
        s = selected[i]
        b = amt.data.edit_bones.new('frag'+str(i))
        b.head = s.location
        b.tail = s.location + mathutils.Vector((0,0.1,0))

    bpy.ops.object.mode_set(mode="OBJECT")
    return amt

def join(selected):
    #bpy.ops.object.select_all(action='DESELECT')
    for i in range(len(selected)):
        s = selected[i]
        s.select_set(True)
    bpy.ops.object.join()

def setPose(amt, selected):
    bpy.context.view_layer.objects.active = amt
    bpy.ops.object.mode_set(mode="POSE")
    for i in range(len(selected)):
        name = "frag" + str(i)
        s = selected[i]
        bone = amt.pose.bones[name]
        bone.location = s.location - amt.data.bones[name].head
        bone.keyframe_insert(data_path="location",group=name)
        bone.rotation_mode = s.rotation_mode
        if bone.rotation_mode == 'QUATERNION':
            bone.rotation_quaternion = s.rotation_quaternion
            bone.keyframe_insert(data_path="rotation_quaternion",group=name)
            print("qua")
        elif bone.rotation_mode == 'AXIS_ANGLE':
            bone.rotation_axis_angle = s.rotation_axis_angle
            bone.keyframe_insert(data_path="rotation_axis_angle",group=name)
            print("axis")
        else:
            bone.rotation_euler = s.rotation_euler
            bone.keyframe_insert(data_path="rotation_euler",group=name)
            print("euler")
            print(s.rotation_euler)
        #bone.lock_location = [True]*3
        #bone.lock_rotation = [True] * 3
        #bone.lock_rotation_w = True
selected = bpy.context.selected_objects
#bpy.ops.object.armature_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
setVertexGroup(selected)
amt = createArmature(selected)

nStart = bpy.context.scene.frame_start
nEnd = bpy.context.scene.frame_end

for t in range(nStart, nEnd + 1):
    #if t % keyframe_freq != 0: continue
    bpy.context.scene.frame_set(t)
    setPose(amt,selected)
    #s.vertex_groups.new(name="frag"+str(i))
    #bpy.ops.object.vertex_group_assign()

#join(selected)    

