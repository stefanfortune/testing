import React from 'react';

export default function SocialPlatformSelector({ 
  selectedPlatforms, 
  onPlatformsChange 
}) {
  const handlePlatformToggle = (platform) => {
    if (selectedPlatforms.includes(platform)) {
      // Remove platform
      onPlatformsChange(selectedPlatforms.filter(p => p !== platform));
    } else {
      // Add platform
      onPlatformsChange([...selectedPlatforms, platform]);
    }
  };

  return (
    <div className="platform-selector">
      <h4>Select Platforms:</h4>
      <div className="platform-options">
        <label>
          <input
            type="checkbox"
            checked={selectedPlatforms.includes('x')}
            onChange={() => handlePlatformToggle('x')}
          />
          X (Twitter)
        </label>
        
        <label>
          <input
            type="checkbox"
            checked={selectedPlatforms.includes('instagram')}
            onChange={() => handlePlatformToggle('instagram')}
          />
          Instagram
        </label>
        
        <label>
          <input
            type="checkbox"
            checked={selectedPlatforms.includes('both')}
            onChange={() => handlePlatformToggle('both')}
          />
          Both Platforms
        </label>
      </div>
    </div>
  );
}