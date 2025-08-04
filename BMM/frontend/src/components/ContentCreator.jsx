import { useState } from 'react';
import { useUser } from '@clerk/clerk-react';
import { useApi } from '../utils/api';

export default function ContentCreator() {
  const { user } = useUser();
  const [content, setContent] = useState({
    raw_text: '',
    media_path: '',
    auto_curate: true,
    tone: 'professional'
  });
  const [generatedCaption, setGeneratedCaption] = useState('');

  const generateCaption = async () => {
    try {
      const businessProfile = await api.getBusinessProfile(user.id);
      const caption = await useApi.generateCaption({
        business_name: businessProfile.business_name,
        business_description: businessProfile.description,
        raw_text: content.raw_text,
        tone: content.tone
      });
      setGeneratedCaption(caption);
    } catch (error) {
      console.error('Error generating caption:', error);
    }
  };

  return (
    <div>
      <textarea
        placeholder="What's your post about?"
        value={content.raw_text}
        onChange={(e) => setContent({...content, raw_text: e.target.value})}
      />
      <input
        type="file"
        onChange={(e) => setContent({...content, media_path: e.target.files[0]})}
      />
      <button onClick={generateCaption}>Generate Caption</button>
      {generatedCaption && (
        <div className="generated-caption">
          <h4>AI-Generated Caption:</h4>
          <p>{generatedCaption}</p>
        </div>
      )}
    </div>
  );
}