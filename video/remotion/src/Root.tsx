import React from 'react';
import {Composition} from 'remotion';
import {Telegram} from './Telegram';

// 7 soniya, 30 fps, vertikal 1080x1920
export const Root: React.FC = () => (
  <Composition id="Telegram" component={Telegram} durationInFrames={210} fps={30} width={1080} height={1920} />
);
