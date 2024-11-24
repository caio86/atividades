import "./ProfileCard.css";

const ProfileCard = ({ name, bio, imageUrl }) => {
  return (
    <div className="profile-card">
      <div>
        <img src={imageUrl} alt={`${name} profile`} />
      </div>
      <h2>{name}</h2>
      <p>{bio}</p>
    </div>
  );
};

export default ProfileCard;
