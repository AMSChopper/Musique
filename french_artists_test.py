import requests
import sys
import time
from datetime import datetime

class FrenchArtistsAPITester:
    def __init__(self, base_url="https://tune-explorer-24.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None):
        """Run a single API test"""
        url = f"{self.api_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=30)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, params=params, timeout=30)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    return True, response_data
                except:
                    return True, response.text
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text[:200]}...")
                self.failed_tests.append({
                    "test": name,
                    "endpoint": endpoint,
                    "expected": expected_status,
                    "actual": response.status_code,
                    "response": response.text[:200]
                })
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append({
                "test": name,
                "endpoint": endpoint,
                "error": str(e)
            })
            return False, {}

    def test_specific_french_artists(self):
        """Test the 15 specific French artists mentioned in requirements"""
        print("\n" + "="*60)
        print("TESTING SPECIFIC FRENCH ARTISTS")
        print("="*60)
        
        # List of 15 French artists from requirements
        french_artists = [
            "Aya Nakamura",
            "Jul", 
            "PNL",
            "Nekfeu",
            "Damso",
            "Orelsan",
            "Booba",
            "Ninho",
            "Maître Gims",
            "MC Solaar",
            "IAM",
            "Tiakola",
            "Niska",
            "Francis Cabrel",
            "Édith Piaf"
        ]
        
        for artist in french_artists:
            success, response = self.run_test(
                f"French Artist Extras - {artist}",
                "GET",
                "artist-extras",
                200,
                params={"name": artist}
            )
            
            if success and isinstance(response, dict):
                found = response.get("found", False)
                anecdotes = response.get("anecdotes", [])
                songs = response.get("songs_written_for_others", [])
                print(f"   Found: {found}, Anecdotes: {len(anecdotes)}, Songs: {len(songs)}")
                
                # Verify specific requirements
                if artist == "Aya Nakamura":
                    if found and len(anecdotes) == 4 and len(songs) >= 6:
                        # Check for Djadja song
                        djadja_found = any("Djadja" in song.get("title", "") for song in songs)
                        print(f"   ✅ Aya Nakamura: 4 anecdotes, 6+ songs, Djadja found: {djadja_found}")
                    else:
                        print(f"   ❌ Aya Nakamura requirements not met: anecdotes={len(anecdotes)}, songs={len(songs)}")
                
                elif artist == "Jul":
                    if found:
                        # Check for Marseille reference in anecdotes
                        marseille_found = any("Marseille" in anecdote for anecdote in anecdotes)
                        print(f"   ✅ Jul: Found with Marseille reference: {marseille_found}")
                    else:
                        print(f"   ❌ Jul not found in database")
                
                elif artist == "PNL":
                    if found:
                        # Check for duo reference (Ademo & N.O.S)
                        duo_found = any("Ademo" in anecdote or "N.O.S" in anecdote for anecdote in anecdotes)
                        print(f"   ✅ PNL: Found with duo reference: {duo_found}")
                    else:
                        print(f"   ❌ PNL not found in database")
                
                elif artist == "Orelsan":
                    if found:
                        # Check for 'Basique' song
                        basique_found = any("Basique" in song.get("title", "") for song in songs)
                        print(f"   ✅ Orelsan: Found with Basique reference: {basique_found}")
                    else:
                        print(f"   ❌ Orelsan not found in database")
                
                elif artist == "Édith Piaf":
                    if found:
                        # Check for 'La Vie en rose'
                        vie_en_rose_found = any("La Vie en rose" in song.get("title", "") for song in songs)
                        print(f"   ✅ Édith Piaf: Found with La Vie en rose reference: {vie_en_rose_found}")
                    else:
                        print(f"   ❌ Édith Piaf not found in database")
                
                else:
                    if found:
                        print(f"   ✅ {artist}: Found in database")
                    else:
                        print(f"   ❌ {artist}: Not found in database")

    def test_youtube_links_in_songs(self):
        """Test that songs have YouTube IDs for inline player"""
        print("\n" + "="*60)
        print("TESTING YOUTUBE LINKS IN GHOSTWRITING SONGS")
        print("="*60)
        
        # Test artists known to have songs with YouTube IDs
        test_artists = ["Ed Sheeran", "Sia", "Aya Nakamura", "Orelsan"]
        
        for artist in test_artists:
            success, response = self.run_test(
                f"YouTube Links - {artist}",
                "GET",
                "artist-extras",
                200,
                params={"name": artist}
            )
            
            if success and isinstance(response, dict):
                songs = response.get("songs_written_for_others", [])
                youtube_songs = [song for song in songs if song.get("youtube_id")]
                print(f"   {artist}: {len(youtube_songs)}/{len(songs)} songs have YouTube IDs")
                
                # Show some examples
                for song in youtube_songs[:2]:
                    print(f"     - {song.get('title')} (ID: {song.get('youtube_id')})")

    def run_all_tests(self):
        """Run all French artists specific tests"""
        print("🇫🇷 FRENCH ARTISTS TESTING STARTED")
        print(f"Testing against: {self.base_url}")
        print("="*60)
        
        start_time = time.time()
        
        # Run test suites
        self.test_specific_french_artists()
        self.test_youtube_links_in_songs()
        
        # Print summary
        end_time = time.time()
        duration = end_time - start_time
        
        print("\n" + "="*60)
        print("🇫🇷 FRENCH ARTISTS TESTING COMPLETED")
        print("="*60)
        print(f"📊 Tests passed: {self.tests_passed}/{self.tests_run}")
        print(f"⏱️  Duration: {duration:.2f} seconds")
        
        if self.failed_tests:
            print(f"\n❌ FAILED TESTS ({len(self.failed_tests)}):")
            for i, test in enumerate(self.failed_tests, 1):
                print(f"{i}. {test['test']}")
                print(f"   Endpoint: {test['endpoint']}")
                if 'error' in test:
                    print(f"   Error: {test['error']}")
                else:
                    print(f"   Expected: {test['expected']}, Got: {test['actual']}")
                print()
        
        success_rate = (self.tests_passed / self.tests_run) * 100 if self.tests_run > 0 else 0
        print(f"✅ Success Rate: {success_rate:.1f}%")
        
        return self.tests_passed == self.tests_run

def main():
    tester = FrenchArtistsAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())