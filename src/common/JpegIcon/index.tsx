import React from 'react';

interface JpegIconProps {
  src: string;
  width: string;
  height: string;
  alt?: string;
}

const JpegIcon = ({ src, width, height, alt }: JpegIconProps) => {
  const altText = alt || src;  // Provide a default alt text if none is provided
  const imagePath = `${process.env.PUBLIC_URL}/img/images/${src}`;  // Construct the image path dynamically

  return (
    <img src={imagePath} alt={altText} width={width} height={height} />
  );
};

export default JpegIcon;  // Use default export here

