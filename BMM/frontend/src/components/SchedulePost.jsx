import { useState } from 'react';
import { useUser } from '@clerk/clerk-react';
import { useApi }  from '../utils/api';
import SocialPlatformSelector from './SocialPlatformSelector';

export default function SchedulePost({ contentId }) {
  const { user } = useUser();
  const [schedule, setSchedule] = useState({
    frequency: 'once',
    platforms: ['x'],
    start_time: '',
    interval_hours: 2,
    random: false
  });

  const handleSchedule = async () => {
    try {
      await useApi.schedulePost({
        content_id: contentId,
        user_id: user.id,
        ...schedule
      });
      alert('Post scheduled successfully!');
    } catch (error) {
      console.error('Error scheduling post:', error);
    }
  };

  return (
    <div>
      <h3>Schedule Post</h3>
      <SocialPlatformSelector 
        selectedPlatforms={schedule.platforms}
        onChange={(platforms) => setSchedule({...schedule, platforms})}
      />
      <select
        value={schedule.frequency}
        onChange={(e) => setSchedule({...schedule, frequency: e.target.value})}
      >
        <option value="once">Once</option>
        <option value="twice">Twice Daily</option>
        <option value="three">Three Times Daily</option>
        <option value="five">Five Times Daily</option>
      </select>
      <input
        type="datetime-local"
        value={schedule.start_time}
        onChange={(e) => setSchedule({...schedule, start_time: e.target.value})}
      />
      <button onClick={handleSchedule}>Schedule Post</button>
    </div>
  );
}