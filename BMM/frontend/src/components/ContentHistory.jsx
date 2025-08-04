import React, { useEffect, useState } from 'react';
import { useUser } from '@clerk/clerk-react';
import { useApi } from '../utils/api';

export default function ContentHistory() {
  const { user } = useUser();
  const [contentList, setContentList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchContent = async () => {
      try {
        const history = await useApi.getContentHistory(user.id);
        setContentList(history);
        setLoading(false);
      } catch (error) {
        console.error('Failed to fetch content history:', error);
      }
    };
    
    fetchContent();
  }, [user.id]);

  if (loading) return <div>Loading content history...</div>;

  return (
    <div className="content-history">
      <h3>Your Content History</h3>
      {contentList.length === 0 ? (
        <p>No content created yet</p>
      ) : (
        <ul>
          {contentList.map(content => (
            <li key={content.id} className="content-item">
              <div className="content-text">{content.text}</div>
              <div className="content-meta">
                <span>{new Date(content.created_at).toLocaleDateString()}</span>
                <span>{content.media_path ? 'With Media' : 'Text Only'}</span>
                <span>{content.posted_to_x ? 'Posted to X' : 'Not Posted'}</span>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}