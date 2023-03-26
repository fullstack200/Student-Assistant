

    def calculateNGrade(self):
        self.percentage = (int(self.scoredMarks / self.total_marks)) * 100
        for g,r in Result.Grade.items():
            if self.percentage in r:
                self.grade = g
                return self.percentage, self.grade
        else:
            self.grade = "Failed"
            return self.percentage, self.grade
        
    def get_subjectsAndTotalMarks(self):
        return self.subjectsAndTotalMarks

    def get_total_marks(self):
        return self.total_marks













