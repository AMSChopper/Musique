import requests
import sys
import json
from datetime import datetime

class MusicHubAPITester:
    def __init__(self, base_url="https://tune-explorer-24.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []
        self.passed_tests = []

    def run_test(self, name, method, endpoint, expected_status, params=None, data=None):
        """Run a single API test"""
        url = f"{self.base_url}/api/{endpoint}"
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
                self.passed_tests.append(name)
                try:
                    response_data = response.json()
                    return True, response_data
                except:
                    return True, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                try:
                    error_detail = response.json()
                    print(f"   Error: {error_detail}")
                except:
                    print(f"   Error: {response.text}")
                self.failed_tests.append({
                    "test": name,
                    "expected": expected_status,
                    "actual": response.status_code,
                    "endpoint": endpoint
                })
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append({
                "test": name,
                "error": str(e),
                "endpoint": endpoint
            })
            return False, {}

    def test_health_endpoints(self):
        """Test basic health endpoints"""
        print("\n=== TESTING HEALTH ENDPOINTS ===")
        self.run_test("API Root", "GET", "", 200)
        self.run_test("Health Check", "GET", "health", 200)

    def test_genius_endpoints(self):
        """Test Genius API integration endpoints"""
        print("\n=== TESTING GENIUS API ENDPOINTS ===")
        
        # Test Genius search
        success, data = self.run_test(
            "Genius Search - Shape of You", 
            "GET", 
            "genius/search", 
            200, 
            params={"q": "Shape of You"}
        )
        if success and data.get("songs"):
            print(f"   Found {len(data['songs'])} songs")
            
        # Test Genius search - Ed Sheeran
        success, data = self.run_test(
            "Genius Search - Ed Sheeran", 
            "GET", 
            "genius/search", 
            200, 
            params={"q": "Ed Sheeran"}
        )
        
        # Test specific song details (Love Yourself by Justin Bieber)
        self.run_test(
            "Genius Song Details - Love Yourself", 
            "GET", 
            "genius/song/2342329", 
            200
        )
        
        # Test artist credits - Ed Sheeran
        success, data = self.run_test(
            "Genius Credits - Ed Sheeran", 
            "GET", 
            "genius/credits", 
            200, 
            params={"artist_name": "Ed Sheeran"}
        )
        if success and data.get("credits"):
            print(f"   Found {len(data['credits'])} credits for Ed Sheeran")
            
        # Test artist credits - Sia
        success, data = self.run_test(
            "Genius Credits - Sia", 
            "GET", 
            "genius/credits", 
            200, 
            params={"artist_name": "Sia"}
        )
        if success and data.get("credits"):
            print(f"   Found {len(data['credits'])} credits for Sia")

    def test_deezer_endpoints(self):
        """Test Deezer API endpoints"""
        print("\n=== TESTING DEEZER API ENDPOINTS ===")
        
        # Test artist search
        success, data = self.run_test(
            "Deezer Artist Search", 
            "GET", 
            "search/artists", 
            200, 
            params={"q": "Ed Sheeran"}
        )
        
        artist_id = None
        if success and data.get("artists"):
            artist_id = data["artists"][0]["id"]
            print(f"   Found artist ID: {artist_id}")
        
        if artist_id:
            # Test artist details
            self.run_test(
                "Deezer Artist Details", 
                "GET", 
                f"artist/{artist_id}", 
                200
            )
            
            # Test artist albums
            self.run_test(
                "Deezer Artist Albums", 
                "GET", 
                f"artist/{artist_id}/albums", 
                200
            )
            
            # Test artist top tracks
            self.run_test(
                "Deezer Artist Top Tracks", 
                "GET", 
                f"artist/{artist_id}/top", 
                200
            )
            
            # Test related artists
            self.run_test(
                "Deezer Related Artists", 
                "GET", 
                f"artist/{artist_id}/related", 
                200
            )

    def test_billboard_endpoints(self):
        """Test Billboard scraping endpoints"""
        print("\n=== TESTING BILLBOARD ENDPOINTS ===")
        
        # Test current Billboard Hot 100
        success, data = self.run_test(
            "Billboard Hot 100 Current", 
            "GET", 
            "billboard/hot100", 
            200
        )
        if success and data.get("songs"):
            print(f"   Found {len(data['songs'])} songs in current chart")
            
        # Test year-end chart
        success, data = self.run_test(
            "Billboard Year-End 2023", 
            "GET", 
            "billboard/year/2023", 
            200
        )
        if success and data.get("songs"):
            print(f"   Found {len(data['songs'])} songs in 2023 year-end chart")

    def test_blindtest_endpoints(self):
        """Test Blind Test endpoints"""
        print("\n=== TESTING BLIND TEST ENDPOINTS ===")
        
        # Test get blind test songs
        success, data = self.run_test(
            "Blind Test Songs", 
            "GET", 
            "blindtest/songs", 
            200, 
            params={"count": 5}
        )
        if success and data.get("songs"):
            print(f"   Generated {len(data['songs'])} blind test questions")
            
        # Test high scores
        self.run_test(
            "Blind Test High Scores", 
            "GET", 
            "blindtest/highscores", 
            200
        )
        
        # Test save score
        self.run_test(
            "Save Blind Test Score", 
            "POST", 
            "blindtest/score", 
            200, 
            params={
                "player_name": "TestPlayer",
                "score": 8,
                "total_questions": 10
            }
        )

    def test_extras_endpoints(self):
        """Test artist extras and credits endpoints"""
        print("\n=== TESTING EXTRAS & CREDITS ENDPOINTS ===")
        
        # Test artist extras (curated data)
        success, data = self.run_test(
            "Artist Extras - Ed Sheeran", 
            "GET", 
            "artist-extras", 
            200, 
            params={"name": "Ed Sheeran"}
        )
        if success:
            print(f"   Found extras: {data.get('found', False)}")
            
        # Test full credits
        success, data = self.run_test(
            "Full Artist Credits", 
            "GET", 
            "credits/artist", 
            200, 
            params={"name": "Ed Sheeran"}
        )
        if success:
            print(f"   Collaborations: {len(data.get('collaborations', []))}")
            print(f"   Writing credits: {len(data.get('writing_credits', []))}")

    def print_summary(self):
        """Print test summary"""
        print(f"\n{'='*50}")
        print(f"📊 TEST SUMMARY")
        print(f"{'='*50}")
        print(f"Total tests: {self.tests_run}")
        print(f"Passed: {self.tests_passed}")
        print(f"Failed: {len(self.failed_tests)}")
        print(f"Success rate: {(self.tests_passed/self.tests_run)*100:.1f}%")
        
        if self.failed_tests:
            print(f"\n❌ FAILED TESTS:")
            for test in self.failed_tests:
                error_msg = test.get('error', f"Expected {test.get('expected')}, got {test.get('actual')}")
                print(f"   - {test['test']}: {error_msg}")
        
        print(f"\n✅ PASSED TESTS:")
        for test in self.passed_tests:
            print(f"   - {test}")
        
        return len(self.failed_tests) == 0

def main():
    print("🎵 Music Hub API Testing Suite")
    print("=" * 50)
    
    tester = MusicHubAPITester()
    
    # Run all test suites
    tester.test_health_endpoints()
    tester.test_genius_endpoints()
    tester.test_deezer_endpoints()
    tester.test_billboard_endpoints()
    tester.test_blindtest_endpoints()
    tester.test_extras_endpoints()
    
    # Print summary
    all_passed = tester.print_summary()
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())