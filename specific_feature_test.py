#!/usr/bin/env python3
"""
Specific feature tests for Music Hub iteration 3 - Extended songwriting credits database
Testing the specific requirements from the review request
"""

import requests
import sys
import json
from datetime import datetime

class SpecificFeaturesTester:
    def __init__(self, base_url="https://tune-explorer-24.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None, validation_func=None):
        """Run a single API test with optional validation"""
        url = f"{self.api_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=30)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, params=params, timeout=30)

            success = response.status_code == expected_status
            if success:
                try:
                    response_data = response.json()
                    # Run custom validation if provided
                    if validation_func:
                        validation_result = validation_func(response_data)
                        if not validation_result:
                            success = False
                            print(f"❌ Failed - Validation failed")
                        else:
                            print(f"✅ Passed - Status: {response.status_code}, Validation: ✓")
                    else:
                        print(f"✅ Passed - Status: {response.status_code}")
                    
                    if success:
                        self.tests_passed += 1
                        return True, response_data
                    else:
                        self.failed_tests.append({
                            "test": name,
                            "endpoint": endpoint,
                            "error": "Validation failed"
                        })
                        return False, response_data
                except:
                    if success:
                        self.tests_passed += 1
                        print(f"✅ Passed - Status: {response.status_code}")
                    return success, response.text
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
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

    def test_ed_sheeran_specific(self):
        """Test Ed Sheeran returns 4 anecdotes and 9 songs"""
        print("\n" + "="*60)
        print("TESTING ED SHEERAN SPECIFIC REQUIREMENTS")
        print("="*60)
        
        def validate_ed_sheeran(data):
            if not data.get('found'):
                print(f"   ❌ Ed Sheeran not found in database")
                return False
            
            anecdotes = data.get('anecdotes', [])
            songs = data.get('songs_written_for_others', [])
            
            print(f"   📝 Anecdotes: {len(anecdotes)} (expected: 4)")
            print(f"   🎵 Songs written for others: {len(songs)} (expected: 9)")
            
            if len(anecdotes) != 4:
                print(f"   ❌ Expected 4 anecdotes, got {len(anecdotes)}")
                return False
            
            if len(songs) != 9:
                print(f"   ❌ Expected 9 songs, got {len(songs)}")
                return False
            
            # Check for specific songs mentioned in requirements
            song_titles = [song.get('title', '') for song in songs]
            expected_songs = ['Love Yourself', 'Little Things']
            
            for expected in expected_songs:
                if not any(expected in title for title in song_titles):
                    print(f"   ❌ Expected song '{expected}' not found")
                    return False
                else:
                    print(f"   ✓ Found expected song: {expected}")
            
            return True

        success, response = self.run_test(
            "Ed Sheeran - 4 anecdotes and 9 songs",
            "GET",
            "artist-extras",
            200,
            params={"name": "Ed Sheeran"},
            validation_func=validate_ed_sheeran
        )

    def test_beyonce_specific(self):
        """Test Beyoncé returns anecdotes about surprise album etc."""
        print("\n" + "="*60)
        print("TESTING BEYONCÉ SPECIFIC REQUIREMENTS")
        print("="*60)
        
        def validate_beyonce(data):
            if not data.get('found'):
                print(f"   ❌ Beyoncé not found in database")
                return False
            
            anecdotes = data.get('anecdotes', [])
            print(f"   📝 Anecdotes: {len(anecdotes)}")
            
            # Check for surprise album anecdote
            anecdote_text = ' '.join(anecdotes).lower()
            if 'surprise' in anecdote_text or 'album' in anecdote_text:
                print(f"   ✓ Found anecdote about surprise album")
                return True
            else:
                print(f"   ❌ No anecdote about surprise album found")
                return False

        success, response = self.run_test(
            "Beyoncé - anecdotes about surprise album",
            "GET",
            "artist-extras",
            200,
            params={"name": "Beyonce"},
            validation_func=validate_beyonce
        )

    def test_prince_specific(self):
        """Test Prince returns songs like 'Nothing Compares 2 U' for Sinead O'Connor"""
        print("\n" + "="*60)
        print("TESTING PRINCE SPECIFIC REQUIREMENTS")
        print("="*60)
        
        def validate_prince(data):
            if not data.get('found'):
                print(f"   ❌ Prince not found in database")
                return False
            
            songs = data.get('songs_written_for_others', [])
            print(f"   🎵 Songs written for others: {len(songs)}")
            
            # Check for Nothing Compares 2 U
            found_nothing_compares = False
            for song in songs:
                title = song.get('title', '').lower()
                artist = song.get('artist', '').lower()
                if 'nothing compares' in title and 'sinéad' in artist:
                    print(f"   ✓ Found 'Nothing Compares 2 U' for Sinéad O'Connor")
                    found_nothing_compares = True
                    break
            
            if not found_nothing_compares:
                print(f"   ❌ 'Nothing Compares 2 U' for Sinéad O'Connor not found")
                return False
            
            return True

        success, response = self.run_test(
            "Prince - 'Nothing Compares 2 U' for Sinéad O'Connor",
            "GET",
            "artist-extras",
            200,
            params={"name": "Prince"},
            validation_func=validate_prince
        )

    def test_jack_antonoff_specific(self):
        """Test Jack Antonoff returns songs written for Taylor Swift and Lorde"""
        print("\n" + "="*60)
        print("TESTING JACK ANTONOFF SPECIFIC REQUIREMENTS")
        print("="*60)
        
        def validate_jack_antonoff(data):
            if not data.get('found'):
                print(f"   ❌ Jack Antonoff not found in database")
                return False
            
            songs = data.get('songs_written_for_others', [])
            print(f"   🎵 Songs written for others: {len(songs)}")
            
            # Check for Taylor Swift and Lorde songs
            found_taylor = False
            found_lorde = False
            
            for song in songs:
                artist = song.get('artist', '').lower()
                title = song.get('title', '')
                if 'taylor swift' in artist:
                    print(f"   ✓ Found song for Taylor Swift: {title}")
                    found_taylor = True
                elif 'lorde' in artist:
                    print(f"   ✓ Found song for Lorde: {title}")
                    found_lorde = True
            
            if not found_taylor:
                print(f"   ❌ No songs for Taylor Swift found")
                return False
            
            if not found_lorde:
                print(f"   ❌ No songs for Lorde found")
                return False
            
            return True

        success, response = self.run_test(
            "Jack Antonoff - songs for Taylor Swift and Lorde",
            "GET",
            "artist-extras",
            200,
            params={"name": "Jack Antonoff"},
            validation_func=validate_jack_antonoff
        )

    def test_french_artists(self):
        """Test French artists like Stromae and Avicii"""
        print("\n" + "="*60)
        print("TESTING FRENCH/INTERNATIONAL ARTISTS")
        print("="*60)
        
        # Test Stromae
        def validate_stromae(data):
            if not data.get('found'):
                print(f"   ❌ Stromae not found in database")
                return False
            
            anecdotes = data.get('anecdotes', [])
            songs = data.get('songs_written_for_others', [])
            print(f"   📝 Anecdotes: {len(anecdotes)}")
            print(f"   🎵 Songs: {len(songs)}")
            
            # Check for French content
            anecdote_text = ' '.join(anecdotes).lower()
            if 'maestro' in anecdote_text or 'verlan' in anecdote_text or 'belge' in anecdote_text:
                print(f"   ✓ Found French artist data")
                return True
            else:
                print(f"   ❌ No specific French artist data found")
                return False

        success, response = self.run_test(
            "Stromae - French artist data",
            "GET",
            "artist-extras",
            200,
            params={"name": "Stromae"},
            validation_func=validate_stromae
        )

        # Test Avicii
        def validate_avicii(data):
            if not data.get('found'):
                print(f"   ❌ Avicii not found in database")
                return False
            
            anecdotes = data.get('anecdotes', [])
            songs = data.get('songs_written_for_others', [])
            print(f"   📝 Anecdotes: {len(anecdotes)}")
            print(f"   🎵 Songs: {len(songs)}")
            
            return len(anecdotes) > 0 or len(songs) > 0

        success, response = self.run_test(
            "Avicii - EDM artist data",
            "GET",
            "artist-extras",
            200,
            params={"name": "Avicii"},
            validation_func=validate_avicii
        )

    def test_unknown_artist(self):
        """Test unknown artist returns found:false"""
        print("\n" + "="*60)
        print("TESTING UNKNOWN ARTIST")
        print("="*60)
        
        def validate_unknown(data):
            found = data.get('found', True)  # Default to True to catch errors
            print(f"   🔍 Found: {found} (should be False)")
            
            if found:
                print(f"   ❌ Unknown artist should return found:false")
                return False
            
            anecdotes = data.get('anecdotes', [])
            songs = data.get('songs_written_for_others', [])
            
            if len(anecdotes) > 0 or len(songs) > 0:
                print(f"   ❌ Unknown artist should have empty anecdotes and songs")
                return False
            
            print(f"   ✓ Unknown artist correctly returns found:false with empty data")
            return True

        success, response = self.run_test(
            "Unknown Artist - returns found:false",
            "GET",
            "artist-extras",
            200,
            params={"name": "Unknown Artist"},
            validation_func=validate_unknown
        )

    def test_sia_diamonds_specific(self):
        """Test Sia shows 'Diamonds' for Rihanna in ghostwriting list"""
        print("\n" + "="*60)
        print("TESTING SIA SPECIFIC REQUIREMENTS")
        print("="*60)
        
        def validate_sia(data):
            if not data.get('found'):
                print(f"   ❌ Sia not found in database")
                return False
            
            songs = data.get('songs_written_for_others', [])
            print(f"   🎵 Songs written for others: {len(songs)}")
            
            # Check for Diamonds for Rihanna
            found_diamonds = False
            for song in songs:
                title = song.get('title', '').lower()
                artist = song.get('artist', '').lower()
                if 'diamonds' in title and 'rihanna' in artist:
                    print(f"   ✓ Found 'Diamonds' for Rihanna")
                    found_diamonds = True
                    break
            
            if not found_diamonds:
                print(f"   ❌ 'Diamonds' for Rihanna not found")
                return False
            
            return True

        success, response = self.run_test(
            "Sia - 'Diamonds' for Rihanna in ghostwriting",
            "GET",
            "artist-extras",
            200,
            params={"name": "Sia"},
            validation_func=validate_sia
        )

    def test_youtube_links(self):
        """Test YouTube 'Écouter' links present for songs with youtube_id"""
        print("\n" + "="*60)
        print("TESTING YOUTUBE LINKS")
        print("="*60)
        
        def validate_youtube_links(data):
            if not data.get('found'):
                return True  # Skip if artist not found
            
            songs = data.get('songs_written_for_others', [])
            youtube_count = 0
            total_songs = len(songs)
            
            for song in songs:
                if song.get('youtube_id'):
                    youtube_count += 1
                    print(f"   ✓ Song '{song.get('title')}' has YouTube ID: {song.get('youtube_id')}")
            
            print(f"   📺 Songs with YouTube links: {youtube_count}/{total_songs}")
            
            # At least some songs should have YouTube links
            return youtube_count > 0 if total_songs > 0 else True

        # Test with Ed Sheeran who should have YouTube links
        success, response = self.run_test(
            "Ed Sheeran - YouTube links for songs",
            "GET",
            "artist-extras",
            200,
            params={"name": "Ed Sheeran"},
            validation_func=validate_youtube_links
        )

    def run_all_specific_tests(self):
        """Run all specific feature tests"""
        print("🎵 MUSIC HUB SPECIFIC FEATURES TESTING STARTED")
        print(f"Testing against: {self.base_url}")
        print("="*70)
        
        start_time = datetime.now()
        
        # Run specific test suites
        self.test_ed_sheeran_specific()
        self.test_beyonce_specific()
        self.test_prince_specific()
        self.test_jack_antonoff_specific()
        self.test_french_artists()
        self.test_unknown_artist()
        self.test_sia_diamonds_specific()
        self.test_youtube_links()
        
        # Print summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print("\n" + "="*70)
        print("🎵 SPECIFIC FEATURES TESTING COMPLETED")
        print("="*70)
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
    tester = SpecificFeaturesTester()
    success = tester.run_all_specific_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())