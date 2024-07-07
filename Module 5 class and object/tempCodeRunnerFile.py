d_teacher(self, name, subj):
        id = len(self.teacher_list)+101
        tea = Teacher(name, subj, id)
        self.teacher_list.append(tea)
