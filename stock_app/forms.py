from .models import *
from django import forms


# 👉 to add stock
class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        
        for instance in Stock.objects.all():
            if instance.category == category:
                raise forms.ValidationError(str(category) + ' is already created')
        return category
    

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name



# 👉 to search stock
class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name']





# 👉 to update stock
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']





# 👉 issue form
class IssueForm(forms.ModelForm):
    	class Meta:
            model = Stock
            fields = ['issue_quantity', 'issue_to']





# 👉 receive form
class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']






# 👉 reorder items form
class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']