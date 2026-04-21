def after_scenario(context, scenario):
    if hasattr(context, "driver"): # Check if the driver attribute exists
        context.driver.quit() # Quit the driver to close the browser after each scenario
        