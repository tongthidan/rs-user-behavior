import logging

from common.constants import ValueContext


class CollaborativeFilter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def get_behavior_context_name(value):
        like = ['1', '0']
        comment = ['1', '0']

        if len([s for s in like if value in s]) > 0:
            return 'is_like'

        if len([s for s in comment if value in s]) > 0:
            return 'is_comment'

        return 'is_post'

    @staticmethod
    def get_condition_data(self, value_of_context):
        try:
            len_context = len(value_of_context)
            result = []
            if len_context == 0:
                return result
            if len_context == 1:
                for i in range(0, len(value_of_context[0])):
                    v1 = ValueContext()
                    v1.name = CollaborativeFilter.get_behavior_context_name(value_of_context[0][i])
                    v1.value = value_of_context[0][i]
                    cons = [v1]
                    result.append(cons)
                return result
            if len_context == 2:
                for i in range(0, len(value_of_context[0])):
                    for j in range(0, len(value_of_context[1])):
                        v1 = ValueContext()
                        v1.name = CollaborativeFilter.get_behavior_context_name(value_of_context[0][i])
                        v1.value = value_of_context[0][i]

                        v2 = ValueContext()
                        v2.name = CollaborativeFilter.get_behavior_context_name(value_of_context[1][j])
                        v2.value = value_of_context[1][j]

                        cons = [v1, v2]

                        result.append(cons)
                return result
            if len_context == 3:
                for i in range(0, len(value_of_context[0])):
                    for j in range(0, len(value_of_context[1])):
                        for k in range(0, len(value_of_context[2])):
                            v1 = ValueContext()
                            v1.name = CollaborativeFilter.get_behavior_context_name(value_of_context[0][i])
                            v1.value = value_of_context[0][i]

                            v2 = ValueContext()
                            v2.name = CollaborativeFilter.get_behavior_context_name(value_of_context[1][j])
                            v2.value = value_of_context[1][j]

                            v3 = ValueContext()
                            v3.name = CollaborativeFilter.get_behavior_context_name(value_of_context[2][k])
                            v3.value = value_of_context[2][k]

                            cons = [v1, v2, v3]

                            result.append(cons)
                return result

        except Exception as e:
            self.logger.exception(e)
