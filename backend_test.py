import requests
import sys
import time
from datetime import datetime

class MusicHubAPITester:
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
                    if isinstance(response_data, dict):
                        print(f"   Response keys: {list(response_data.keys())}")
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

    def test_health_endpoints(self):
        """Test basic health endpoints"""
        print("\n" + "="*50)
        print("TESTING HEALTH ENDPOINTS")
        print("="*50)
        
        self.run_test("API Root", "GET", "", 200)
        self.run_test("Health Check", "GET", "health", 200)

    def test_artist_search(self):
        """Test artist search functionality"""
        print("\n" + "="*50)
        print("TESTING ARTIST SEARCH")
        print("="*50)
        
        # Test with popular artists
        test_queries = ["Daft Punk", "Rihanna", "Ed Sheeran", "Adele"]
        
        for query in test_queries:
            success, response = self.run_test(
                f"Search Artists - {query}",
                "GET",
                "search/artists",
                200,
                params={"q": query}
            )
            if success and isinstance(response, dict):
                artists = response.get("artists", [])
                if artists:
                    print(f"   Found {len(artists)} artists")
                    # Test getting details for first artist
                    first_artist = artists[0]
                    artist_id = first_artist.get("id")
                    if artist_id:
                        self.test_artist_details(artist_id, first_artist.get("name", "Unknown"))
                else:
                    print(f"   No artists found for {query}")

    def test_artist_details(self, artist_id, artist_name):
        """Test artist details endpoints"""
        print(f"\n--- Testing Artist Details for {artist_name} (ID: {artist_id}) ---")
        
        # Test artist details
        success, response = self.run_test(
            f"Get Artist Details - {artist_name}",
            "GET",
            f"artist/{artist_id}",
            200
        )
        
        # Test artist albums
        self.run_test(
            f"Get Artist Albums - {artist_name}",
            "GET",
            f"artist/{artist_id}/albums",
            200
        )
        
        # Test artist top tracks
        self.run_test(
            f"Get Artist Top Tracks - {artist_name}",
            "GET",
            f"artist/{artist_id}/top",
            200
        )

    def test_billboard_endpoints(self):
        """Test Billboard chart endpoints"""
        print("\n" + "="*50)
        print("TESTING BILLBOARD ENDPOINTS")
        print("="*50)
        
        # Test current Hot 100
        success, response = self.run_test(
            "Billboard Hot 100 - Current",
            "GET",
            "billboard/hot100",
            200
        )
        if success and isinstance(response, dict):
            songs = response.get("songs", [])
            print(f"   Found {len(songs)} songs in current chart")
        
        # Test year-end charts for recent years
        current_year = datetime.now().year
        test_years = [current_year - 1, 2020, 2015]
        
        for year in test_years:
            success, response = self.run_test(
                f"Billboard Year-End {year}",
                "GET",
                f"billboard/year/{year}",
                200
            )
            if success and isinstance(response, dict):
                songs = response.get("songs", [])
                print(f"   Found {len(songs)} songs for {year}")

    def test_blindtest_endpoints(self):
        """Test Blind Test game endpoints"""
        print("\n" + "="*50)
        print("TESTING BLIND TEST ENDPOINTS")
        print("="*50)
        
        # Test getting blind test songs
        success, response = self.run_test(
            "Get Blind Test Songs",
            "GET",
            "blindtest/songs",
            200,
            params={"count": 5}
        )
        if success and isinstance(response, dict):
            songs = response.get("songs", [])
            print(f"   Got {len(songs)} blind test songs")
            if songs:
                first_song = songs[0]
                print(f"   First song has YouTube ID: {first_song.get('youtube_id')}")
                print(f"   First song has {len(first_song.get('choices', []))} choices")
        
        # Test saving a score
        test_player = f"test_player_{int(time.time())}"
        success, response = self.run_test(
            "Save Blind Test Score",
            "POST",
            "blindtest/score",
            200,
            params={
                "player_name": test_player,
                "score": 8,
                "total_questions": 10
            }
        )
        
        # Test getting high scores
        success, response = self.run_test(
            "Get High Scores",
            "GET",
            "blindtest/highscores",
            200,
            params={"limit": 10}
        )
        if success and isinstance(response, dict):
            scores = response.get("scores", [])
            print(f"   Found {len(scores)} high scores")

    def test_error_cases(self):
        """Test error handling"""
        print("\n" + "="*50)
        print("TESTING ERROR CASES")
        print("="*50)
        
        # Test invalid artist ID
        self.run_test(
            "Invalid Artist ID",
            "GET",
            "artist/999999999",
            404
        )
        
        # Test invalid year for Billboard
        self.run_test(
            "Invalid Billboard Year",
            "GET",
            "billboard/year/1990",
            400
        )
        
        # Test empty search query
        self.run_test(
            "Empty Search Query",
            "GET",
            "search/artists",
            422,  # FastAPI validation error
            params={"q": ""}
        )

    def run_all_tests(self):
        """Run all test suites"""
        print("🎵 MUSIC HUB API TESTING STARTED")
        print(f"Testing against: {self.base_url}")
        print("="*60)
        
        start_time = time.time()
        
        # Run test suites
        self.test_health_endpoints()
        self.test_artist_search()
        self.test_billboard_endpoints()
        self.test_blindtest_endpoints()
        self.test_error_cases()
        
        # Print summary
        end_time = time.time()
        duration = end_time - start_time
        
        print("\n" + "="*60)
        print("🎵 MUSIC HUB API TESTING COMPLETED")
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
    tester = MusicHubAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())