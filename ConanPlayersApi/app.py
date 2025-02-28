from flask import Flask, jsonify
import a2s
import os

app = Flask(__name__)

# Function to load references from a text file
def load_references():
    references = {}
    # Debug: Print the current working directory to ensure the file path is correct
    print(f"Current Working Directory: {os.getcwd()}")
    try:
        with open('references.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    a2s_name, player_friendly_name, guild_name = parts
                    references[a2s_name.strip()] = {
                        'friendly_name': player_friendly_name.strip(),
                        'guild_name': guild_name.strip()
                    }
        print("Loaded references:", references)  # Debug print to help verify the loaded references
    except FileNotFoundError:
        print("Error: 'references.txt' file not found.")
    return references

@app.route('/players/<ip>/<int:port>', methods=['GET'])
def get_conan_exiles_server_player_list(ip, port):
    try:
        server_address = (ip, port)
        player_info = a2s.players(server_address)

        references = load_references()

        # Constructing the enhanced player list with defaults for friendly_name and guild_name
        player_list = []
        for player in player_info:
            ref_data = references.get(player.name.strip(), {})
            player_data = {
                'name': player.name,
                'score': player.score,
                'duration': player.duration,
                # Use data from references if available; otherwise, use defaults
                'friendly_name': ref_data.get('friendly_name', 'Unknown'),
                'guild_name': ref_data.get('guild_name', 'No Guild')
            }
            player_list.append(player_data)

        return jsonify(player_list)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
