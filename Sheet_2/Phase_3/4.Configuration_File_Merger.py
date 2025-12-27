import json

def merge_configs(default_config, user_config):
    merged_config = default_config.copy()
    
    for key, value in user_config.items():
        if key in merged_config and isinstance(value, dict) and isinstance(merged_config[key], dict):
            merged_config[key] = merge_configs(merged_config[key], value)
        else:
            merged_config[key] = value

    return merged_config

def main():
    
    default_config = json.loads(input("Enter the default configuration file: "))
    user_config = json.loads(input("Enter the user configuration file: "))

    result = merge_configs(default_config, user_config)
    print(result)

main()
    