import unittest
from tests import PluginTest
from plugins.ytdownload import YTDownload


class YTDownloadTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(YTDownload)  # Load the plugin class

    def test_download_command(self):
        # Example test input and expected output — adjust for your plugin
        test_input = "download https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        expected_output = "Downloading video from YouTube..."

        # Run the plugin with the test input
        self.test.run(test_input)

        # Assert the plugin responded correctly
        self.assertEqual(self.history_say().last_text(), expected_output)


if __name__ == '__main__':
    unittest.main()