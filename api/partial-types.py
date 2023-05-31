from prisma_client import models

# Get all the model names defined in the 'models' module
model_names = [name for name in dir(models) if name[0].isupper()]

# Create partials for each model
for model_name in model_names:
    # Get the model class dynamically using the model name
    model_class = getattr(models, model_name)
    
    # Create the partial for the model
    model_class.create_partial(model_name + 'x')