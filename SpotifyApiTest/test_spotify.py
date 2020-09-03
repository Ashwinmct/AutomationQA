import requests
import json


class TestSpotify:
	base_url = 'https://api.spotify.com/'
	success_status_value = 200
	failure_status_value = 401
	details = {
		'Authorization': 'Bearer BQCmTNBcagyoA5kSutAunuWE6ITQ16sX8cY9Kry_yBmUBr2VH2KVtq4WE0EwMXVk2aUBXgEDxOECEKnRXCeujOlz0V2tcCPTfIm295gn8GOmd_c2eBhKcPGrE17BTWW4xePfeyBAKBHQWpbiusKCvzoMfEQxrqSQSXsEKtLrfmhKFsdZo3Qi3cSpUADXhtGSvTsi4weD6vIeynh0W2_DcWle0LHBMBNkXKmyjR1eCmKYBQBm5rQ9mEiErJl5jLZiCyMGns8QIhlRLjToDAVYWhcL7WcGl62f'
	}
	user_id_for_test = 'c3c3iq3mx29p1kmc5rqjtmms6'
	user_name_for_test = 'AshwinMcp'

	def test_given_api_with_correct_url_when_connected_should_return_success_status_code(self):
		expected_status_code = self.success_status_value
		response_received = requests.get(self.base_url)
		assert response_received.status_code == expected_status_code

	def test_given_api_with_wrong_url_when_connected_should_return_invalid_status_code(self):
		wrong_url = self.base_url + "a2b\\"
		response_received = requests.get(wrong_url)
		assert response_received.status_code == self.failure_status_value

	def test_given_api_with_valid_token_when_connected_should_return_success_status_code(self):
		testing_url = self.base_url+'v1/me'
		response_received = requests.get(url=testing_url, headers=self.details)
		assert response_received.status_code == self.success_status_value

	def test_given_api_with_invalid_token_when_connected_should_return_failure_status_code(self):
		testing_url = self.base_url+'v1/me'
		details = {
			'Authorization': 'Bearer BzD'
		}
		response_received = requests.get(url=testing_url, headers=details)
		assert response_received.status_code == self.failure_status_value

	def test_given_api_with_valid_token_when_connected_should_return_current_user_name(self):
		testing_url = self.base_url+'v1/me'
		expected_user_name = 'AshwinMcp'
		response_received = requests.get(url=testing_url, headers=self.details)
		recieved_user_name = response_received.json().get('display_name')
		assert recieved_user_name == expected_user_name

	def test_given_api_with_valid_token_when_connected_should_return_current_user_id(self):
		global user_id
		testing_url = self.base_url+'v1/me'
		response_received = requests.get(url=testing_url, headers=self.details)
		user_id = response_received.json().get('id')
		assert user_id == self.user_id_for_test

	def test_given_api_with_valid_user_id_when_connected_should_return_respected_user_details(self):
		testing_url = self.base_url+'v1/users/'+user_id
		response_received = requests.get(url=testing_url, headers=self.details)
		recieved_user_name = response_received.json().get('display_name')
		assert recieved_user_name == self.user_name_for_test

	def test_for_given_name_playlist_when_created_should_create_a_new_playlist(self):
		global total_playlists, playlist_id
		playlist_addition_url = self.base_url+'v1/users/' + user_id + '/playlists'
		playlist_details = {"name": "Ashwin","description": "added playlist for testing", "public": False}
		playlist_count_received_before_adding_new_playlist = self.get_total_playlist_count()
		response_received = requests.post(url=playlist_addition_url, headers=self.details, data=json.dumps(playlist_details))
		playlist_id = response_received.json().get('id')
		total_playlists = self.get_total_playlist_count()
		assert total_playlists == (playlist_count_received_before_adding_new_playlist + 1)

	def test_given_user_id_when_connected_should_return_respected_users_playlist(self):
		test_url = self.base_url + 'v1/users/' + user_id + '/playlists'
		response_received = requests.get(url=test_url,headers=self.details)
		expected_playlists_count = total_playlists
		received_playlists_count = response_received.json().get("total")
		assert received_playlists_count == expected_playlists_count

	def test_given_playlist_api_when_connected_should_return_current_users_playlist(self):
		expected_playlists_count = total_playlists
		received_playlists_count = self.get_total_playlist_count()
		assert received_playlists_count == expected_playlists_count

	def get_total_playlist_count(self):
		test_url = self.base_url+'v1/me/playlists'
		return requests.get(url=test_url, headers=self.details).json().get('total')
