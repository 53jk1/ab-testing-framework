import random
from scipy import stats
import pandas as pd

class ABTest:
    def __init__(self, variants, duration, significance_level):
        self.variants = variants
        self.duration = duration
        self.significance_level = significance_level
        self.data = pd.DataFrame(columns=['user_id', 'variant', 'conversion'])

    def assign_user(self, user_id):
        variant = random.choice(self.variants)
        self.data = self.data.append({'user_id': user_id, 'variant': variant, 'conversion': 0}, ignore_index=True)
        return variant

    def register_conversion(self, user_id):
        self.data.loc[self.data['user_id'] == user_id, 'conversion'] = 1

    def analyze_results(self):
        results = {}

        for variant in self.variants:
            results[variant] = self.data[self.data['variant'] == variant]['conversion'].mean()

        control_group = results[self.variants[0]]
        experimental_group = results[self.variants[1]]
        p_value = stats.ttest_ind(
            self.data[self.data['variant'] == self.variants[0]]['conversion'],
            self.data[self.data['variant'] == self.variants[1]]['conversion']
        ).pvalue

        return {
            'control_group': control_group,
            'experimental_group': experimental_group,
            'p_value': p_value,
            'is_significant': p_value < self.significance_level
        }
